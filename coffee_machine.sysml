package coffee_machine {
  block CoffeeMachine {
    name: "Coffee Machine";
    description: "A simple coffee machine model.";
    property 'param:brew_time': Integer = 30; // seconds
  }

  block WaterTank {
    name: "Water Tank";
    description: "Holds the water for brewing.";
    property 'param:capacity': Integer = 1000; // Milliliters
    property 'state:current_level': Integer = 0;
  }

  block Grinder {
    name: "Grinder";
    description: "Grinds the coffee beans.";
    property 'param:grind_setting': Integer = 3;
  }

  block UI {
    name: "User Interface";
    description: "Controls the machine.";
    property 'state:button_pressed': Boolean = false;
  }

  connect WaterTank to CoffeeMachine;
  connect Grinder to CoffeeMachine;
  connect UI to CoffeeMachine;
}