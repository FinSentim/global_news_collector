import unittest
from GlobalNewsCollector.Germany.managerMagazin import managerMagazin
from datetime import date

class TestScrapper(unittest.TestCase):

    def test_get_articles_list(self):
        url = "https://www.manager-magazin.de/"
        list = managerMagazin.get_articles_list(managerMagazin,url)
        self.assertEqual(len(list),44)
        

    def test_get_article(self):
        url = "https://www.manager-magazin.de/harvard/selbstmanagement/selbstmanagement-wie-sie-sich-dazu-bringen-schwierige-dinge-anzugehen-a-115ecb8c-9380-45d3-9ed6-9a00897259f2"
        dict = managerMagazin.get_article(managerMagazin,url)
        correct_dict = {
            "date_published" : "2022-01-26",
            "date_retrieved" : date.today().strftime("%Y-%m-%d"),
            "url" : "https://www.manager-magazin.de/harvard/selbstmanagement/selbstmanagement-wie-sie-sich-dazu-bringen-schwierige-dinge-anzugehen-a-115ecb8c-9380-45d3-9ed6-9a00897259f2",
            "title" : "Selbstmanagement: Wie Sie sich dazu bringen, schwierige Dinge anzugehen",
            "publisher" : "manager magazin",
            "publisher_url" : "https://www.manager-magazin.de/",
            "author" : "David Rock, manager magazin",
            "body" : "Wenn man sich umhört, wie die Stimmungslage in diesen Tagen ist, heißt die Antwort meist: 'erschöpft'. Wir sind es leid, inmitten großer Ungewissheit zu arbeiten. Ermattet davon, Kinderbetreuung und Arbeit unter einen Hut zu bekommen. Und müde vor lauter Personalengpässen und Lieferkettenproblemen.Wenn wir uns so fühlen, will unser Gehirn Energie sparen, indem es sich auf die am leichtesten verfügbaren, abrufbaren Informationen konzentriert, damit wir schnell Entscheidungen treffen können. Wir hören deshalb oft auf unser Bauchgefühl oder treffen Entscheidungen nach Vermutungen. Man nennt das 'Expediency Bias': wir machen, was sich richtig anfühlt oder legen uns fest, ohne alle Fakten zu kennen, wir handeln also zweckmäßig. Unser Gehirn verarbeitet bestehende Ideen viel einfacher als neue, in der Psychologie auch Fluency-Effekt genannt. Das ist der Grund, warum es viel einfacher ist, Italienisch zu lernen als Japanisch, wenn man Spanisch spricht. Und auch warum viele Menschen zwei Ein-Dollar-Scheine für wertvoller halten als einen Zwei-Dollar-Schein, wie der Marketingprofessor Adam Alter erklärt.Das führt dazu, dass viele von uns von Natur aus dazu neigen, das zu tun, was sich richtig anfühlt - sei es, dass wir unser Team bitten, wieder ins Büro zu kommen, weil unser Gehirn sich das vorstellen kann, oder dass wir davon ausgehen, dass alle eine Viertagewoche wollen. Hier kommt auch das hedonistische Prinzip ins Spiel: Wir sind so verdrahtet, dass wir uns zu Dingen hinbewegen, die uns ein gutes Gefühl geben, und uns von Dingen entfernen, die uns Unbehagen bereiten. Unser Gehirn stuft Anstrengung als schlecht ein, weil sie harte Arbeit ist.Unser Gehirn orientiert sich an dem Standard, was sich 'normal' anfühlt - an den Netzwerken, die uns sagen, wie wir uns durch unseren Alltag navigieren sollten. Diese Netzwerke sind so tief in unserem Denken verankert, dass selbst, wenn wir einen neuen und herausfordernden Weg einschlagen - ganz gleich, um welchen Weg es sich handelt -, wir wieder in alte Bahnen zurückkehren.Und doch wissen wir, dass harte Veränderungen enorme Vorteile haben können - die vielleicht erst nach einiger Zeit sichtbar werden. Denken Sie an den Beginn eines neuen Sportprogramms. Vielleicht haben wir eine Einsicht - 'Wenn ich einen Kilometer laufen kann, habe ich mehr Energie, um mit meinen kleinen Kindern zu spielen' -, die uns zum Handeln anspornt. Oder vielleicht hat uns ein Arzt gesagt, dass wir unseren Lebensstil ändern müssen, oder es gibt einen Anreiz, der uns anspornt.Der erste Lauf fühlt sich nicht gut anAber etwas Kurioses kann passieren: Wenn wir den ersten Lauf machen, fühlt er sich nicht gut an. Genauso wenig wie beim nächsten oder übernächsten Lauf. Unsere Muskeln schmerzen. Das Geld, das wir für das neue Hobby ausgegeben haben, führt zu Spannungen in unserem Haushalt. Der Zeitplan hält uns von der wertvollen Zeit ab, die wir früher mit Freunden verbracht haben. Es gibt immer mehr Gründe, warum wir zu den alten Zeiten zurückkehren sollten - als unsere Muskeln nicht schmerzten, als wir mit unseren Freunden etwas trinken gingen, als wir uns nicht mit unseren Partnern stritten, weil wir 70 Euro pro Monat für eine Mitgliedschaft im Fitnessstudio ausgaben.Wie können wir also schwierige Dinge tun, wenn unser Gehirn uns ständig sagt, dass wir uns nicht anstrengen sollen?Erstens, indem wir sie in Angriff nehmen, wenn wir gut gelaunt sind. Eine Studie aus dem Jahr 2016 ergab, dass Menschen, die verärgert sind, seltener versuchen, schwierige Dinge zu tun. Wenn sie jedoch gut gelaunt sind, nehmen sie eher die schwierigen, aber wichtigen Aufgaben in Angriff, die das Leben letztlich verbessern. Eine Möglichkeit, uns in die richtige Stimmung zu bringen, ist die sogenannte 'Neubewertung', bei der wir in unserem Gehirn eine Veränderung der Wahrnehmung einer Aufgabe bewirken. Eine Neubewertung kann effektiv sein, wenn wir ein einfaches, aussagekräftiges Wort oder einen Satz wählen, das oder der unsere Zielvorstellung beschreibt. Wenn Sie sich etwa sagen: 'Ich werde mich besser fühlen, wenn ich diesen neuen Prozess zu Papier bringe', kann das ausreichen, um Ihr Gehirn aus einer unproduktiven Schleife herauszuholen.Zweitens müssen wir unseren Gehirnen das richtige Maß an Autonomie zugestehen. Wenn wir die Wahl haben, entscheidet sich unser Gehirn oft für etwas Einfaches. Aber wir können diese Reaktion abschwächen, indem wir uns selbst herausfordern, innovativ zu sein, und Anreize schaffen. Anstatt zu überlegen, ob wir uns beim Mittagessen für etwas Gesundes entscheiden sollen, sollten wir uns zum Beispiel fragen: Möchte ich diesen frischen Salat, der mir Energie gibt, oder diesen Donut, nach dessen Verzehr mir beim letzten Mal schlecht geworden ist und der mich müde gemacht hat?Im Arbeitskontext: Möchte ich mit einem neuen Projektmanagement-Tool experimentieren, das meinem Team nächste Woche die Arbeit erleichtern könnte, oder möchte ich an der gleichen Tabelle festhalten, die ein ehemaliger Mitarbeiter erstellt hat und mit der ohnehin keiner von uns etwas anfangen kann?Schließlich können wir auch schwierige Dinge erreichen, wenn wir einen 'Growth Mindset' entwickeln und es uns auffällt, wenn wir zurück in alte Muster fallen. Dabei hilft es auch, wenn uns andere immer wieder daran erinnern. Wir sollten uns mit anderen austauschen, und zwar in einer Umgebung, in der die Versuche ebenso geschätzt werden wie die Ergebnisse.Ein Beispiel: Ein Team von Führungskräften hat kürzlich versucht, sich den Vormittag frei von Meetings zuhalten, um in der Zeit konzentriert arbeiten zu können. Einigen gelang das, andere stellten fest, dass ihre Konzentrationsphasen eher am Nachmittag lagen. Nach einem Monat entschieden sie, dass das Experiment gescheitert ist, ihre Zeitpläne waren einfach zu unterschiedlich. Sie wählten eine andere Taktik: Nur die Montagvormittage wurden im Kalender geblockt. Statt zurück in alte Muster zu fallen, erkannten sie an, welchen Fortschritt die neue Gewohnheit gebracht hatte und experimentierten weiter.Dinge zu tun, die sich unangenehm und wie harte Arbeit anfühlen, kann kontraintuitiv erscheinen. Aber wenn wir verstehen, was in unserem Gehirn vor sich geht und nicht nur auf unser Bauchgefühl hören, können wir uns daran gewöhnen, schwierige Aufgaben zu meistern und unsere Ängste besser bewältigen."
            }
        self.assertEqual(dict,correct_dict)
        
       

if __name__ == '__main__':
    unittest.main()