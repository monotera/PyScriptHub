import os
import imageio

clip = os.path.abspath("Dark_2.mp4")  # Nombre del video


def gifMaker(inputPath, targetFormat):
    outputPath = os.path.splitext(inputPath)[0] + targetFormat
    print(f"converting {inputPath} \n to {outputPath}")
    reader = imageio.get_reader(inputPath)
    fps = reader.get_meta_data()["fps"]
    writer = imageio.get_writer(outputPath, fps=fps)
    print("Loading...")
    for frames in reader:
        writer.append_data(frames)
    print("Done!")
    writer.close()


gifMaker(clip, ".gif")
