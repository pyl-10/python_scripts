from subprocess import run

input_video = '/Users/***/Downloads/GUI/1、色彩属性和原理/2、色彩的三要素.mp4'
segment_time = 10
m3u8_list = '/Users/***/Downloads/GUI/1、色彩属性和原理/色彩三要素.m3u8'
output_video = '/Users/***/Downloads/GUI/1、色彩属性和原理/video-%04d.ts'
out = '/Users/***/Downloads/GUI/1、色彩属性和原理/out.mp4'

# 拆分视频
cmd1 = ["ffmpeg", "-i", input_video, "-f", "segment", "-segment_time", str(segment_time), "-segment_format",
        "mpegts", "-segment_list", m3u8_list, "-c", "copy", "-bsf:v", "h264_mp4toannexb", "-map", "0", output_video]

run(cmd1)

'''
ffmpeg -allowed_extensions ALL -protocol_whitelist "file,http,crypto,tcp,https" -i index.m3u8 -c copy out.mp4
'''

# 合并视频
cmd2 = ['ffmpeg', '-allowed_extensions', 'ALL', '-protocol_whitelist',
        'file', '-i', m3u8_list, '-c', 'copy', out]
run(cmd2)

# 视频文件的格式分别代表着什么 ?
# mp4 一个单独的视频文件比较大，为了减少视频的加载时间，会先把 一整个 mp4 切分成 一块块的 ts 文件
# ts ts 保证了 多个ts文件连起来的视频无缝播放。
# m3u8 索引文件， 确保一块块的 ts 文件顺序正确。不会乱序错位
