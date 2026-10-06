const preces = [
 { nosaukums: "Klade", cena: 2.5, irPieejama: true },
 { nosaukums: "Pildspalva", cena: 1.2, irPieejama: false },
 { nosaukums: "Mape", cena: 3.0, irPieejama: true }
];

// • Uzraksti funkciju pieejamoPrecuSumma(preces), kas ar ciklu saskaita tikai pieejamo preču cenas un atgriež summu.
// • Izdrukā rezultātu konsolē.
// • Pievieno masīvam vēl vienu pieejamu preci un pārbaudi funkciju vēlreiz

function pieejamoPrecuSumma(preces) {
 let summa = 0;
 for (i = 0; i < preces.length; i++) {
 if (i.irPieejama) summa += i.cena;
 }
 return summa;
}
console.log(pieejamoPrecuSumma(preces)); 
preces.push({ nosaukums: "Lineāls", cena: 1.5, irPieejama: true });
console.log(pieejamoPrecuSumma(preces)); 
