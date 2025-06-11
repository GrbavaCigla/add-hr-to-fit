import argparse
import pathlib

from fit_tool.fit_file import FitFile
from fit_tool.profile.messages.record_message import RecordMessage
from fit_tool.utils.crc import crc16


def calculate_crc(fitfile: FitFile):
    calculated_crc = crc16(fitfile.header.to_bytes(), crc=0)

    for record in fitfile.records:
        calculated_crc = crc16(record.to_bytes(), crc=calculated_crc)

    return calculated_crc


def main(main_path, hr_path, out_path):
    mainfile = FitFile.from_file(main_path)
    hrfile = FitFile.from_file(hr_path)

    hr_data = {
        record.message.timestamp: record.message.heart_rate
        for record in hrfile.records
        if isinstance(record.message, RecordMessage)
    }

    for record in mainfile.records:
        message = record.message

        if (
            isinstance(message, RecordMessage)
            and hr_data.get(message.timestamp) is not None
        ):
            message.heart_rate = hr_data[message.timestamp]

    mainfile.crc = calculate_crc(mainfile)
    mainfile.to_file(out_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="add-hr-to-fit",
        description="Small simple project to add HR data from one activity to"
        " another. Used for when my HR strap stops working.",
    )

    parser.add_argument(
        "main",
        type=pathlib.Path,
        help="file to which the heart data will be added.",
    )
    parser.add_argument(
        "hr",
        type=pathlib.Path,
        help="file which holds heart data.",
    )
    parser.add_argument(
        "out",
        type=pathlib.Path,
        help="output file of the combined activities.",
        nargs="?",
        default="out.fit",
    )

    args = parser.parse_args()

    main(args.main, args.hr, args.out)
