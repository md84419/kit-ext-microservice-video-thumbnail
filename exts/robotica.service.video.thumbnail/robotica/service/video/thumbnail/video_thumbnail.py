from moviepy.editor import VideoFileClip, ImageSequenceClip, VideoClip, concatenate_videoclips


def extract_and_compile_frames(input_path, output_path, target_resolution, num_frames):

    video = VideoFileClip(input_path)

    extracted_frames = []

    frame_interval = video.duration / num_frames
    print(f'video.duration: {video.duration}')
    print(f'num_frames: {num_frames}')
    print(f'frame_interval: {frame_interval}')

    # Calculate the resize parameters
    target_width, target_height = target_resolution
    frame_width, frame_height = video.size
    resize_ratio = min(target_width / frame_width, target_height / frame_height)
    resize_width = int(frame_width * resize_ratio)
    resize_height = int(frame_height * resize_ratio)

    for count in range(num_frames):
        frame_index = count * frame_interval
        print(f'frame_index: {frame_index}')

        extracted_frames.append(video.get_frame(frame_index))

    reframed_clip = ImageSequenceClip(extracted_frames, fps=video.fps)
    # reframed_clip = concatenate_videoclips(extracted_frames, method="compose")

    output_clip: VideoClip = reframed_clip.resize((resize_width, resize_height))

    output_clip.write_videofile(output_path, codec="libx264")
    # output_path.seek(0)

    return output_path
