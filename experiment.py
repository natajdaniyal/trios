def run_test(profile):

    print("\n==============================")
    print("🧪 آزمایش آزمایشی Trios")
    print("==============================")


    prediction = input(
        "\n✍️ فرضیه تو چیست؟ "
    )


    print(
        "\n🔬 آزمایش انجام شد..."
    )


    result = "نیروی وارد شده باعث حرکت جسم شد."


    correct = True


    print(
        "\n🧪 نتیجه:"
    )

    print(result)


    profile.add_experiment(
        "آزمایش آزمایشی نیرو",
        prediction,
        result,
        correct
    )


    print(
        "\n🤖 Trios-Bot:"
    )

    print(
        "گزارش آزمایش ذخیره شد. 🌌"
    )