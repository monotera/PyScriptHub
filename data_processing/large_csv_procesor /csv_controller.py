import dask.dataframe as dd

# Complexity: O(n), where n is the number of rows in the input dataframe.


def process_csv(input_file, output_file):
    # Write the header to the output CSV file
    with open(output_file, "w") as file:
        file.write("Song,Date,Number of Plays\n")  # Complexity: O(1)

    # Read the input CSV file as a Dask dataframe
    df = dd.read_csv(input_file)  # Complexity: O(1)

    # Group by 'Song' and 'Date' columns and sum the 'Number of Plays' column
    # Complexity: O(n), where n is the number of rows in the input dataframe.
    aggregated_df = df.groupby(["Song", "Date"])["Number of Plays"].sum().reset_index()

    # Write the aggregated data to the output CSV file
    # O(m), where m is the number of rows in the aggregated dataframe.
    aggregated_df.to_csv(
        output_file, index=False, header=False, mode="a", single_file=True
    )

    return output_file
