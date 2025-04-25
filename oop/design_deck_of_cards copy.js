// JavaScript (ES6+)

class ICard {
  // Just a marker; no enforcement in plain JS
  stringify() {
    throw new Error("Must override stringify()");
  }
}

class PokerCard extends ICard {
  constructor(suit, value) {
    super();
    this.suit = suit;
    this.value = value;
  }
  stringify() {
    return `${this.value} of ${this.suit}s`;
  }
}

class FlinchCard extends ICard {
  constructor(number) {
    super();
    this.number = number;
  }
  stringify() {
    return `${this.number}`;
  }
}

class Deck {
  constructor() {
    this.cards = [];
  }
  create(cards) {
    this.cards = cards.slice();
  }
  take() {
    return this.cards.pop();
  }
  look() {
    return this.cards[this.cards.length - 1].stringify();
  }
}

// Usage
const cards = [new PokerCard("club", "three"), new PokerCard("heart", "four")];
const deck = new Deck();
deck.create(cards);
console.log(deck.look()); // -> "four of hearts"
