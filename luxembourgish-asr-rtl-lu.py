#!/usr/bin/env python3
#
#  Created by lemswasabi on 17/05/2022.
#  Copyright © 2022 letzspeak. All rights reserved.
#
"""Luxembourgish ASR RTL.lu Dataset"""


import os

import datasets

from datasets.tasks import AutomaticSpeechRecognition


_DESCRIPTION = """\
luxembourgish-asr-rtl-lu dataset is a speech corpus for the under-resourced Luxembourgish language.
"""

_URLS = {
    "rtl-benchmark": "https://drive.google.com/uc?id=1IiFV6TZHH1sOBL409VnmxCXSSyQkue0F&export=download&confirm=t",
}

class Tuudle(datasets.GeneratorBasedBuilder):

    VERSION = datasets.Version("1.1.0")

    BUILDER_CONFIGS = [
        datasets.BuilderConfig(name="rtl-benchmark", version=VERSION, description="This part contains benchmark of samples collected from the RTL.lu domain"),
    ]

    DEFAULT_CONFIG_NAME = "tuudle"

    def _info(self):

        features = datasets.Features(
            {
                "audio": datasets.Audio(sampling_rate=16_000),
                "sentence": datasets.Value("string"),
            }
        )

        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=features,
            supervised_keys=("audio", "sentence"),
            task_templates=[AutomaticSpeechRecognition(audio_column="audio", transcription_column="sentence")],
        )

    def _split_generators(self, dl_manager):

        urls = _URLS[self.config.name]
        archive_path  = dl_manager.download_and_extract(urls)
        metadata_filepaths = {
            split: os.path.join(archive_path, os.path.join(split, f"{split}.tsv"))
            for split in ["train", "test", "dev"]
        }

        return [
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN,
                gen_kwargs={
                    "local_extracted_archive": archive_path,
                    "metadata_filepath": metadata_filepaths["train"],
                    "split": "train",
                },
            ),
            datasets.SplitGenerator(
                name=datasets.Split.TEST,
                gen_kwargs={
                    "local_extracted_archive": archive_path,
                    "metadata_filepath": metadata_filepaths["test"],
                    "split": "test",
                },
            ),
            datasets.SplitGenerator(
                name=datasets.Split.VALIDATION,
                gen_kwargs={
                    "local_extracted_archive": archive_path,
                    "metadata_filepath": metadata_filepaths["dev"],
                    "split": "dev",
                },
            ),
        ]

    def _generate_examples(self, local_extracted_archive, metadata_filepath, split):

        path_to_clips  = os.path.join(local_extracted_archive, split)

        with open(metadata_filepath, encoding="utf-8") as f:
            lines = f.readlines()
            for key, line in enumerate(lines[1:]):
                field_values = line.strip().split("\t")
                if len(field_values) == 2:
                    audio_filename, sentence = field_values[0], field_values[1]
                    audio_path = os.path.join(path_to_clips, audio_filename)
                    yield key, {
                        "audio": {"path": audio_path, "bytes": open(audio_path, "rb").read()},
                        "sentence": sentence,
                    }
