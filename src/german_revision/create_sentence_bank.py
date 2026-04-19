import json
from pathlib import Path

# create_sentence_bank.py

sentence_bank = {
"basic V2" : [
    "Ich gehe heute ins Kino.",
    "Du lernst jeden Abend Deutsch.",
    "Er spielt am Wochenende Fußball.",
    "Wir trinken morgens Kaffee.",
    "Sie arbeitet in einem Büro.",
    "Ich lese gern Bücher.",
    "Du kaufst heute Brot.",
    "Er besucht seine Freunde oft.",
    "Wir fahren morgen nach Berlin.",
    "Sie schreibt eine E-Mail.",
    "Ich esse gern Pizza.",
    "Du trinkst jeden Morgen Tee.",
    "Er arbeitet heute im Büro.",
    "Wir spielen am Abend Karten.",
    "Sie kauft im Supermarkt ein.",
    "Ich höre gern Musik.",
    "Du siehst jeden Tag fern.",
    "Er fährt jeden Morgen zur Arbeit.",
    "Wir lernen zusammen Deutsch.",
    "Sie liest am Wochenende ein Buch."
],

"time-manner-place" :  [
    "Ich gehe heute mit dem Bus zur Arbeit.",
    "Du lernst jeden Tag mit deiner Freundin Deutsch.",
    "Er fährt am Wochenende mit dem Zug nach Hamburg.",
    "Wir essen heute Abend in einem Restaurant.",
    "Sie arbeitet jeden Morgen im Büro.",
    "Ich spiele am Nachmittag mit meinen Freunden Fußball.",
    "Du gehst heute zu Fuß zur Schule.",
    "Er liest am Abend im Bett ein Buch.",
    "Wir fahren morgen mit dem Auto nach München.",
    "Sie trinkt morgens in der Küche Kaffee.",
    "Ich gehe heute mit meiner Schwester ins Kino.",
    "Du arbeitest jeden Tag im Büro.",
    "Er fährt morgen mit dem Fahrrad zur Arbeit.",
    "Wir lernen heute Abend in der Bibliothek Deutsch.",
    "Sie spielt am Wochenende mit ihren Freunden Tennis.",
    "Ich esse heute Mittag in der Kantine.",
    "Du gehst jeden Morgen mit dem Hund spazieren.",
    "Er liest heute Nachmittag im Park ein Buch.",
    "Wir fahren am Sonntag mit dem Zug nach Köln.",
    "Sie trinkt am Morgen im Büro Tee."
],

" subject inversion" : [
    "Heute gehe ich ins Kino.",
    "Morgen fahren wir nach Berlin.",
    "Am Abend liest er ein Buch.",
    "Im Sommer reisen wir nach Spanien.",
    "Nach der Arbeit trinke ich Kaffee.",
    "Am Wochenende spielt er Fußball.",
    "Jetzt lerne ich Deutsch.",
    "Dann gehen wir nach Hause.",
    "Später rufe ich dich an.",
    "Heute Abend essen wir zusammen.",
    "Heute arbeite ich im Büro.",
    "Morgen schreibe ich eine Prüfung.",
    "Am Morgen trinke ich Tee.",
    "Im Winter fahre ich Ski.",
    "Nach dem Essen gehe ich spazieren.",
    "Am Nachmittag spiele ich Tennis.",
    "Jetzt mache ich meine Hausaufgaben.",
    "Dann sehe ich fern.",
    "Später lese ich ein Buch.",
    "Heute treffe ich meine Freunde."
],

"modal verbs" : [
    "Ich will heute ins Kino gehen.",
    "Du musst jeden Tag Deutsch lernen.",
    "Er kann gut Fußball spielen.",
    "Wir wollen morgen nach Berlin fahren.",
    "Sie soll mehr Wasser trinken.",
    "Ich darf heute länger aufbleiben.",
    "Du musst das Buch lesen.",
    "Er will seine Freunde besuchen.",
    "Wir können heute Abend essen gehen.",
    "Sie will eine E-Mail schreiben.",
    "Ich kann heute nicht kommen.",
    "Du willst morgen früh aufstehen.",
    "Er muss heute lange arbeiten.",
    "Wir dürfen heute nicht ausgehen.",
    "Sie kann sehr gut singen.",
    "Ich will ein neues Buch kaufen.",
    "Du musst mehr Wasser trinken.",
    "Er kann das Problem lösen.",
    "Wir wollen zusammen lernen.",
    "Sie muss ihre Hausaufgaben machen."
],

"perfect tense" : [
    "Ich habe gestern einen Film gesehen.",
    "Du hast viel Deutsch gelernt.",
    "Er ist nach Berlin gefahren.",
    "Wir haben zusammen gegessen.",
    "Sie hat ein Buch gelesen.",
    "Ich habe meine Freunde besucht.",
    "Du bist früh nach Hause gegangen.",
    "Er hat Fußball gespielt.",
    "Wir haben Kaffee getrunken.",
    "Sie ist im Park spazieren gegangen.",
    "Ich habe gestern Musik gehört.",
    "Du hast ein interessantes Buch gelesen.",
    "Er ist zur Arbeit gefahren.",
    "Wir haben einen Kuchen gebacken.",
    "Sie hat lange geschlafen.",
    "Ich habe das Fenster geöffnet.",
    "Du bist spät angekommen.",
    "Er hat einen Brief geschrieben.",
    "Wir sind ins Kino gegangen.",
    "Sie hat einen Film gesehen."
],

"subordinate clause" : [
    "Ich weiß, dass du heute kommst.",
    "Er sagt, dass er müde ist.",
    "Wir glauben, dass sie recht hat.",
    "Sie denkt, dass ich komme.",
    "Ich hoffe, dass du Zeit hast.",
    "Er weiß, dass wir morgen fahren.",
    "Wir sehen, dass er lernt.",
    "Sie sagt, dass sie arbeitet.",
    "Ich denke, dass es stimmt.",
    "Du glaubst, dass ich recht habe.",
    "Ich weiß, dass er hier ist.",
    "Er denkt, dass wir gewinnen.",
    "Wir hoffen, dass du kommst.",
    "Sie glaubt, dass es möglich ist.",
    "Ich sehe, dass du arbeitest.",
    "Er sagt, dass sie kommt.",
    "Wir wissen, dass es stimmt.",
    "Sie denkt, dass er müde ist.",
    "Ich hoffe, dass alles gut geht.",
    "Du weißt, dass ich recht habe."
],

"seperable verb" : [
    "Ich stehe jeden Morgen früh auf.",
    "Du kaufst heute im Supermarkt ein.",
    "Er ruft seine Mutter an.",
    "Wir gehen heute Abend aus.",
    "Sie kommt spät nach Hause zurück.",
    "Ich mache das Fenster auf.",
    "Du räumst dein Zimmer auf.",
    "Er lädt seine Freunde ein.",
    "Wir steigen in den Zug ein.",
    "Sie zieht ihre Jacke aus.",
    "Ich stehe um sieben Uhr auf.",
    "Du kaufst Brot im Laden ein.",
    "Er ruft seinen Freund an.",
    "Wir gehen am Wochenende aus.",
    "Sie kommt heute spät zurück.",
    "Ich mache die Tür auf.",
    "Du räumst die Küche auf.",
    "Er lädt seine Familie ein.",
    "Wir steigen am Bahnhof ein.",
    "Sie zieht ihren Mantel aus."
],

"negation" : [
    "Ich gehe heute nicht ins Kino.",
    "Du lernst nicht genug Deutsch.",
    "Er spielt heute nicht Fußball.",
    "Wir fahren morgen nicht nach Berlin.",
    "Sie arbeitet nicht im Büro.",
    "Ich esse heute kein Fleisch.",
    "Du hast keine Zeit.",
    "Er trinkt keinen Kaffee.",
    "Wir sehen den Film nicht.",
    "Sie kauft das Buch nicht.",
    "Ich komme heute nicht.",
    "Du arbeitest nicht viel.",
    "Er fährt heute nicht zur Arbeit.",
    "Wir gehen heute nicht aus.",
    "Sie liest das Buch nicht.",
    "Ich habe keine Lust.",
    "Du hast kein Geld.",
    "Er kauft keinen Kuchen.",
    "Wir trinken keinen Alkohol.",
    "Sie sieht den Film nicht."
]
}

hard_sentence_bank = {
    "basic V2" : [
    "Ich schreibe heute meiner Schwester einen langen Brief.",
    "Du erklärst dem Lehrer morgen das schwierige Problem.",
    "Er zeigt seinem Freund am Abend das neue Spiel.",
    "Wir bringen unserer Mutter heute Blumen nach Hause.",
    "Sie erzählt den Kindern am Abend eine spannende Geschichte.",
    "Ich gebe dem Mann an der Kasse das Geld.",
    "Du liest deiner kleinen Schwester eine Geschichte vor.",
    "Er kauft seiner Freundin morgen ein schönes Geschenk.",
    "Wir schicken unserem Lehrer heute eine wichtige E-Mail.",
    "Sie erklärt den Studenten das komplizierte Thema."
],
    "time-manner-place" : [
    "Ich gehe heute mit meiner Schwester mit dem Bus zur Arbeit.",
    "Du lernst jeden Abend mit großer Konzentration in der Bibliothek Deutsch.",
    "Er fährt morgen früh mit dem Zug nach Berlin.",
    "Wir arbeiten heute den ganzen Tag mit hoher Motivation im Büro.",
    "Sie spielt am Wochenende mit ihren Freunden im Park Tennis.",
    "Ich lese heute Abend mit großem Interesse zu Hause ein Buch.",
    "Du gehst morgen früh mit deinem Hund im Park spazieren.",
    "Er arbeitet jeden Tag mit seinem Kollegen im Büro.",
    "Wir fahren am Sonntag mit dem Auto nach München.",
    "Sie trinkt jeden Morgen in der Küche mit ihrer Familie Kaffee."
],
   "inversion" : [
    "Heute schreibe ich meiner Schwester einen langen Brief.",
    "Morgen erkläre ich dem Lehrer das schwierige Problem.",
    "Am Abend zeigt er seinem Freund das neue Spiel.",
    "Nach der Arbeit bringen wir unserer Mutter Blumen nach Hause.",
    "Am Wochenende erzählt sie den Kindern eine spannende Geschichte.",
    "Heute gebe ich dem Mann an der Kasse das Geld.",
    "Am Abend liest du deiner kleinen Schwester eine Geschichte vor.",
    "Morgen kauft er seiner Freundin ein schönes Geschenk.",
    "Heute schicken wir unserem Lehrer eine wichtige E-Mail.",
    "Im Unterricht erklärt sie den Studenten das komplizierte Thema."
],
   "modal verbs" : [
    "Ich will meiner Schwester heute einen langen Brief schreiben.",
    "Du musst dem Lehrer morgen das schwierige Problem erklären.",
    "Er kann seinem Freund am Abend das neue Spiel zeigen.",
    "Wir wollen unserer Mutter heute Blumen nach Hause bringen.",
    "Sie soll den Kindern am Abend eine spannende Geschichte erzählen.",
    "Ich muss dem Mann an der Kasse das Geld geben.",
    "Du kannst deiner kleinen Schwester eine Geschichte vorlesen.",
    "Er will seiner Freundin morgen ein schönes Geschenk kaufen.",
    "Wir müssen unserem Lehrer heute eine wichtige E-Mail schicken.",
    "Sie kann den Studenten das komplizierte Thema erklären."
],
   "perfect tense" : [
    "Ich habe meiner Schwester gestern einen langen Brief geschrieben.",
    "Du hast dem Lehrer heute das schwierige Problem erklärt.",
    "Er hat seinem Freund am Abend das neue Spiel gezeigt.",
    "Wir haben unserer Mutter Blumen nach Hause gebracht.",
    "Sie hat den Kindern eine spannende Geschichte erzählt.",
    "Ich habe dem Mann an der Kasse das Geld gegeben.",
    "Du hast deiner kleinen Schwester eine Geschichte vorgelesen.",
    "Er hat seiner Freundin ein schönes Geschenk gekauft.",
    "Wir haben unserem Lehrer eine wichtige E-Mail geschickt.",
    "Sie hat den Studenten das komplizierte Thema erklärt."
],
   "subordinate clause" : [
    "Ich weiß, dass du meiner Schwester heute einen langen Brief schreibst.",
    "Er sagt, dass du dem Lehrer morgen das schwierige Problem erklärst.",
    "Wir glauben, dass er seinem Freund am Abend das neue Spiel zeigt.",
    "Sie denkt, dass wir unserer Mutter heute Blumen nach Hause bringen.",
    "Ich hoffe, dass sie den Kindern am Abend eine spannende Geschichte erzählt.",
    "Er weiß, dass ich dem Mann an der Kasse das Geld gebe.",
    "Wir sehen, dass du deiner kleinen Schwester eine Geschichte vorliest.",
    "Sie sagt, dass er seiner Freundin morgen ein schönes Geschenk kauft.",
    "Ich denke, dass wir unserem Lehrer heute eine wichtige E-Mail schicken.",
    "Du glaubst, dass sie den Studenten das komplizierte Thema erklärt."
],
   "seperable verb" : [
    "Ich schreibe meiner Schwester heute einen langen Brief auf.",
    "Du rufst deinen Freund am Abend an.",
    "Er lädt seine Freunde am Wochenende zu sich nach Hause ein.",
    "Wir bringen die Gäste am Abend nach Hause zurück.",
    "Sie stellt das Buch ins Regal zurück.",
    "Ich mache am Morgen das Fenster weit auf.",
    "Du räumst dein Zimmer am Wochenende gründlich auf.",
    "Er kauft im Supermarkt frisches Brot ein.",
    "Wir steigen am Bahnhof in den Zug ein.",
    "Sie zieht am Abend ihre warme Jacke aus."
],
   "negation" : [
    "Ich schreibe meiner Schwester heute keinen langen Brief.",
    "Du erklärst dem Lehrer morgen das schwierige Problem nicht.",
    "Er zeigt seinem Freund am Abend das neue Spiel nicht.",
    "Wir bringen unserer Mutter heute keine Blumen nach Hause.",
    "Sie erzählt den Kindern am Abend keine spannende Geschichte.",
    "Ich gebe dem Mann an der Kasse das Geld nicht.",
    "Du liest deiner kleinen Schwester keine Geschichte vor.",
    "Er kauft seiner Freundin morgen kein schönes Geschenk.",
    "Wir schicken unserem Lehrer heute keine wichtige E-Mail.",
    "Sie erklärt den Studenten das komplizierte Thema nicht."
]
    }
'''
def normalise_sentences(sentence_dict: dict[str, list]) -> dict[str, list]:
    norm_sentences = {}
    for k, v in sentence_dict.items():
        sentence_list = []
        for s in v:
            ns = s.strip().lower()
            sentence_list.append(ns)
        norm_sentences[k] = sentence_list
    return norm_sentences

normalised_sentence_bank = normalise_sentences(sentence_bank)

normalised_hard_sentence_bank = normalise_sentences(hard_sentence_bank)
  '''          
    
    
    
    
path = Path("data/sentence_bank.json")
# save
path.write_text(json.dumps(sentence_bank, indent=2, ensure_ascii=False), encoding="utf-8")


path = Path("data/hard_sentence_bank.json")
path.write_text(json.dumps(sentence_bank, indent=2, ensure_ascii=False), encoding="utf-8")


