import sys
def get_rpc_update():
    if sys.platform in ['Windows', 'win32', 'cygwin']:
        try:
            from api.windows import get_title, get_process_info, get_status

            app_info = get_process_info()
            app_title = get_title(app_info['pid'])
            app_state = get_status(app_info, app_title)

            rpc_update = {'state': app_state,
                          'small_image': app_info['smallImageKey'],
                          'large_image': app_info['largeImageKey'],
                          'large_text': app_info['largeText'],
                          'small_text': app_info['smallText'],
                          'details': app_info['largeText']}
            return rpc_update

        except ImportError:
            print("Make sure you have pywin32 installed")

    elif sys.platform in ['Mac', 'darwin', 'os2', 'os2emx']:
        print("you are such a fucking loser")
        try:
            app_info = "i am using mac"
            app_title = "im loser lol"
            app_state = "go use a proper computer"

            rpc_update = {'state': app_state,
                          'small_image': "photoshop_small",
                          'large_image': "photoshop_large",
                          'large_text': "imagine using macbook",
                          'small_text': "go use a proper computer",
                          'details': "i am a loser cuz i use mac"}
            return rpc_update
        except ImportError:
            print("you disingenius dense motherfucker")
    else:
        print("stupid arch user lmao")


def exception_handler(exception, future):
    print("")
