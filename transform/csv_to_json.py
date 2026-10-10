import pandas as pd


def transform_csv_to_json(csv_input_path: str, json_output_path: str) -> None:
    df = pd.read_csv(csv_input_path, sep=',')
    print("DF LOADED")

    df.to_json(json_output_path, orient="records", lines=True)
    print("Exported to NDJSON successfully!")
    print(f"NDJSON file in path {json_output_path}")


if __name__ == "__main__":
    input_file_paths = [
        'files/VA_PPSample25.csv',
        "files/FHA_PPSample25.csv",
        "files/CONV_30ITMSample25.csv"
    ]
    output_file_paths = [
        'files/VA_PPSample25.json',
        "files/FHA_PPSample25.json",
        "files/CONV_30ITMSample25.json"
    ]
    
    # for i in range(len(input_file_paths)):
    #     transform_csv_to_json(input_file_paths[i], output_file_paths[i])

    transform_csv_to_json("data/FHA_PPSample25.csv", "data/l0_federal_data.json")