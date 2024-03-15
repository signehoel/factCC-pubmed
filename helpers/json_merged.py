import json


def merge_json(files, input_dir, output_dir, output_filename):
    all_items = []
    for file in files:
        with open(f"{input_dir}/{file}") as textfile:
            for line in textfile:
                all_items.append(json.loads(line))

    with open(f"{output_dir}/{output_filename}", "w") as textfile_merged:
        for item in all_items:
            textfile_merged.write(json.dumps(item) + "\n")
    print(
        f"Successfully merged {len(all_items)} items into {output_dir}/{output_filename}"
    )


def main():
    files = [
        "data-valid-positive.jsonl",
        "data-valid-negative.jsonl",
        "data-valid-positive-noise.jsonl",
        "data-valid-negative-noise.jsonl",
    ]
    input_dir = "pubmed/valid"  # Change this to the desired input directory
    output_dir = "pubmed/valid"  # Change this to the desired output directory
    output_filename = "data-valid.jsonl"  # Change this to the desired output filename
    merge_json(files, input_dir, output_dir, output_filename)


if __name__ == "__main__":
    main()
