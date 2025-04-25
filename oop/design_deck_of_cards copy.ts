// TypeScript

interface ICard {
  stringify(): string;
}

class PokerCard implements ICard {
  constructor(private suit: string, private value: string) {}

  stringify(): string {
    return `${this.value} of ${this.suit}s`;
  }
}

class FlinchCard implements ICard {
  constructor(private number: number) {}

  stringify(): string {
    return `${this.number}`;
  }
}

class Deck {
  private cards: ICard[] = [];

  create(cards: ICard[]): void {
    this.cards = [...cards];
  }

  take(): ICard {
    return this.cards.pop()!;
  }

  look(): string {
    return this.cards[this.cards.length - 1].stringify();
  }
}

// Usage
const cards: ICard[] = [
  new PokerCard("club", "three"),
  new PokerCard("heart", "four"),
];
const deck = new Deck();
deck.create(cards);
console.log(deck.look()); // -> "four of hearts"
