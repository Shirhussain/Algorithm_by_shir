/*
Design a coffee machine

Ingredients? 
- Espresso
- Steamed Milk
- Hot Water

Cappuccino
Small
- 1 espresso
- 4oz milk
- scoop of foam

Medium
- 2 espresso
- 8oz milk
- scoop of foam

Latte
Small
- 1 espresso
- 6oz milk
- small scoop of foam

Medium
- 2 espresso
- 14oz milk
- small scoop of foam

Americano
Small
- 1 espresso
- 6oz hotwater

Medium
- 2 espresso
- 14oz hotwater


Espresso
- 1 espresso

Topping or Mixins?
No

Different cup sizes?
No

Price?
Yes, for future

Machine

*/

public abstract class Ingredient {
  String name;

  
  
}

public class Recipe {
  Map<Ingredient, Integer> ingredientMap = new HashMap<>();

  public Recipe(Map<Ingredient, Integer> ingredientMap) {
    this.ingredientMap = ingredientMap;
  }
}

public class Milk extends Ingredient {
  
}

public class Water extends Ingredient {
  
}

public class EspressoIngredient extends Ingredient {
  
}

public class IngredientInventory {
  Map<Ingredient, Integer> ingredientInventoryMap = new HashMap<>();

  public addIngredient(Ingredient ingredient, int volume) {}

  public getIngredient(Ingredient ingredient, int volume) {}

  public minimumLevelsAvailable(Drink drink) {}
  
}

public abstract class Drink {
  String name;
  protected Recipe recipe;
  double price;
  Size size;

  public Drink(string drinkName, double price) {
    this.name = drinkName;
    this.price = price;
  }

  public abstract Drink process();
}

public enum Size {
  SMALL,
  MEDIUM,
  LARGE
}

public class Americano extends Drink {
  public Americano(String name, double price) {
    this.generateRecipe()
  }

  private void generateRecipe() {
    Map<Ingredient, Integer> ingredientMap = new HashMap<>();
    ingredientMap.put(new Water("Water"), new Integer(6));
    ingredientMap.put(new Espresso("Espresso"), new Integer(1));
    
    Recipe recipe = new Recipe(ingredientMap);
    this.recipe = recipe;
  }

  addMixins()
  
}

public class Cappuccino extends Drink {
  public Cappuccino(String name, double price) {
    this.generateRecipe()
  }

  private void generateRecipe() {
    Map<Ingredient, Integer> ingredientMap = new HashMap<>();
    if (this.size == Size.SMALL) {
      ingredientMap.put(new Milk("Milk"), new Integer(4));
      ingredientMap.put(new Espresso("Espresso"), new Integer(1));
    }
    else if (this.size == Size.MEDIUM) {
      ingredientMap.put(new Milk("Milk"), new Integer(8));
      ingredientMap.put(new Espresso("Espresso"), new Integer(2));
    }
    else if (this.size == Size.LARGE) {
      ingredientMap.put(new Milk("Milk"), new Integer(10));
      ingredientMap.put(new Espresso("Espresso"), new Integer(2));
    }
    
    Recipe recipe = new Recipe(ingredientMap);
    this.recipe = recipe;
  }
}

public class Machine {
  IngredientInventory ingredientInventory;
  public void generateDrink(Drink drink) {
    Recipe recipe = drink.getRecipe();
    
    Map<Ingredient, Integer> ingredientMap = ingredientInventory.getInventory().ingredientInventoryMap;
    
  }
}


class Main {
  public static void main(String[] args) {
    System.out.println("Hello world!");
  }
}