Feature: produce video thumbnails from videos

  Scenario: run a simple test
      Given a video
       When we call the service
       Then we get a thumbnail video

  Scenario Outline: we can produce thumbnails for MP4, MOV and MKV video formats
      Given a video in the format <format>
       When we call the service
       Then we get a thumbnail video
  Examples:
     | format |
     | MP4    |
     | MOV    |
     | MKV    |

  Scenario Outline: we can produce valid thumbnails regardless of the input resolution and aspect ratio
      Given a video with x resolution <x>
        And y resolution <y>
       When we call the service
       Then we get a thumbnail video
  Examples:
     | x      | y     |
     | 1920   | 1080  |
     | 600    | 400   |
     | 200    | 150   |
     | 1080   | 1920  |
     | 400    | 600   |
     | 150    | 200   |

  Scenario Outline: we can produce thumbnails regardless of the framerate
      Given a video with framerate <framerate>
       When we call the service
       Then we get a thumbnail video
  Examples:
     | framerate |
     | 60        |
     | 30        |
     | 24        |

  # Note: 16s video is at 16 fps, i.e. excatly 256 frames long
  # Durations here are h(ours), m(inutes), s(econds) and f(rames)
  Scenario Outline: we can produce thumbnails regardless of the duration
      Given a video of <duration> seconds
       When we call the service
       Then we get a thumbnail video
  Examples:
     | duration |
     | 16s      |
     | 8s       |
     | 32s      |
     | 1f       |
     | 1h       |
  
  # This scenario is for information only
  # The implementation of "we get a thumbnail video" implements
  # this Then clause completely
  Scenario: validate thumbnail video: "thumbnail video" means a resolution of 256x256 which is exactly 256 frames long
      Given a video
       When we call the service
       Then we get a thumbnail video
        And the thumbnail video has a resolution of 256x256
        And the thumbnail video is exactly 256 frames long

  Scenario Outline: video production is pathological
      Given a video
       When we call the service
        And when we call the serivce a second time
       Then we get a thumbnail video
        And we get another thumbnail video
        And the two thumbnail videos are identical
