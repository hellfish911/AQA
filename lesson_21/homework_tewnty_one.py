"""This module processes the log file."""

from datetime import datetime


def analyze_heartbeat_log(input_file, output_file, key="Key TSTFEED0300|7E3E|0400"):
    """
    Analyze a log file for heartbeat intervals and logs warnings or errors.

    Parameters:
        input_file (str): Path to the input log file.
        output_file (str): Path to the output log file where results will be written.
        key (str): The specific key to filter log entries for analysis.
    """
    filtered_log = []

    with open(input_file, "r") as file:
        for line in file:
            if key in line:
                filtered_log.append(line.strip())

    with open(output_file, "w") as log_file:
        for i in range(len(filtered_log) - 1):

            timestamp_1_idx = filtered_log[i].find("Timestamp ")
            timestamp_2_idx = filtered_log[i + 1].find("Timestamp ")

            if timestamp_1_idx != -1 and timestamp_2_idx != -1:
                time_1 = datetime.strptime(
                    filtered_log[i][timestamp_1_idx + 10:timestamp_1_idx + 18], "%H:%M:%S"
                )
                time_2 = datetime.strptime(
                    filtered_log[i + 1][timestamp_2_idx + 10:timestamp_2_idx + 18], "%H:%M:%S"
                )

                heartbeat_diff = (time_1 - time_2).total_seconds()
                if heartbeat_diff < 0:
                    heartbeat_diff += 86400

                if 31 < heartbeat_diff < 33:
                    log_file.write(
                        f"WARNING: Heartbeat {heartbeat_diff:.1f} seconds at {filtered_log[i]}\n"
                    )
                elif heartbeat_diff >= 33:
                    log_file.write(
                        f'ERROR: Heartbeat {heartbeat_diff:.1f} seconds at {filtered_log[i]}\n'
                    )


if __name__ == '__main__':
    analyze_heartbeat_log('hblog.txt', 'hb_test.log')
