// Online Java Compiler
// Use this editor to write, compile and run your Java code online
import java.util.Vector;

interface ICard
{
    // interface means list of all methods or functoins
    public String stringify();
}

class PokerCard implements ICard
{
    private String suit;
    private String value;
    
    public PokerCard(String suit, String value)
    {
        this.suit = suit;
        this.value = value;
    }
    public String stringify()
    {
        return value + " of " + suit + "s";
    }
}
class FlinchCard implements ICard
{
    private int number;
    public FlinchCard(int number)
    {
        this.number = number;
    }
    
    public String stringify()
    {
        return "" + number;
    }
}
class Deck
{
    private Vector<ICard> cards;
    
    public void create(ICard[] cards)
    {
        this.cards = new Vector<ICard>();
        for (ICard card : cards)
        {
            this.cards.add(card);   
        }
    }
    public ICard take() {
        ICard card = cards.remove(cards.size()-1);
        return card;
    }
    
    public String look()
    {
        return cards.get(cards.size()-1).stringify();
    }
}
class Main {
    public static void main(String[] args) {
        ICard[] cards = new PokerCard[2];
        cards[0] = new PokerCard("club", "three");
        cards[1] = new PokerCard("heart", "four");
        Deck deck = new Deck();
        deck.create(cards);
        System.out.println(deck.look());
        
    }
}



