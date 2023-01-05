from cli_functions import get_album_data


def main():
    running = True
    welcome_one = "Welcome to Photo Explore CLI"
    welcome_two = "You can browse photo information by entering the album ID (e.x 4) or a range of IDs (ex 4-6)"

    print(welcome_one.center(40, '*'))
    print(welcome_two.center(40), "\n")

    while running:

        user_album_request = input("Enter the Album ID or range of IDs you would like to explore: ")

        album_json = get_album_data(user_album_request)

        if len(album_json) < 1:
            print(f"Whoops! No results were found for Album selection {user_album_request}")
        else:
            print(f"Album selection {user_album_request} contains {len(album_json)} photos")
            for photo in album_json:
                print(f"[{photo['id']}]: {photo['title']}")

        user_continue_prompt = input("Would you like to make another selection?(y/n): ")

        if 'n' in user_continue_prompt:
            running = False


if __name__ == '__main__':
    main()
