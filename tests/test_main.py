from ml_engineering_foundations import main


def test_main_prints_greeting(capsys):
    main()

    assert (
        capsys.readouterr().out
        == "Hello from ml-engineering-foundations!\n"
    )
