Dany jest plik tekstowy, zawierający przedziały liczbowe w zakresie `<-100,100>`

Definicja: Przedziały ograniczone

Niech   a i b będą dowolnymi liczbami rzeczywistymi, przy czym a<b.

–   Przedziałem obustronnie otwartym nazywamy zbiór  liczb   rzeczywistych
spełniających warunek   `a < x < b`. Przedział ten oznaczamy `(a, b)`.

–   Przedziałem obustronnie domkniętym nazywamy zbiór    liczb   rzeczywistych x spełniających warunek `a ≤ x ≤ b`. Przedział ten oznaczamy `<a , b>`.

–   Przedziałem lewostronnie domkniętym nazywamy zbiór    liczb   rzeczywistych x spełniającychwaruneka `≤ x < b`. Przedział ten oznaczamy `<a, b)`.

–   Przedziałem prawostronnie domkniętym nazywamy zbiór    liczb    rzeczywistych  x spełniających warunek `a < x ≤ b`. Przedział ten oznaczamy `(a , b>`.

Plik  przedzialy.txt zawiera 50  informacji o  przedziałach, po  jednym w  każdym wierszu. Każdy    przedział jest   zapisany w  formacie: znak   otwartego lub   domkniętego przedziału, wartość   a, znak    przecinka, wartość b, znak   otwartego lub  domkniętego przedziału (patrz    przykład);
wartości a i b są liczbami całkowitymi z zakresu `<–100, 100>`.

Przykład zestawu danych:
`(–2,5>  
<–3,2>
`

Napisz program, który wczyta te dane i zwróci listę zawierającą 50 list, które zawierają odpowiednie liczby z przedziałów, np. :
`
[
[ -1, 0, 1, 2, 3, 4, 5],
[ -3, -2, -1, 0, 1, 2],
]
`