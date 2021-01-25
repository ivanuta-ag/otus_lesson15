def test_main_page(main_page):
    main_page.wait_for_download()
    main_page.check_wish_list()
    main_page.check_len_menu_items()
    main_page.navbar()
    main_page.check_logo()
    main_page.check_cart()
