from robotic_code_representation_generator import RoboticCodeRepresentationGenerator


def main():
    commands_order = ["LEFT", "GRAB", "LEFT", "BACK", "LEFT", "BACK", "LEFT"]
    generator = RoboticCodeRepresentationGenerator(commands_order)
    print(generator.get_rcr("GRAB"))
    print(generator.get_rcr("BACK"))
    print(generator.get_rcr("LEFT"))


if __name__ == '__main__':
    main()


