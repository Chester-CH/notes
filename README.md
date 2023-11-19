## Notes sovellus

Käyttäjän tulee ensin rekisteröityä ja kirjautua sisään, ja sen jälkeen käyttäjä voi luoda muistiinpanoja ja antaa niille otsikoita.

Käyttäjä voi luoda, muokata ja poistaa muistiinpanoja.

Käyttäjä voi järjestää muistiinpanot esimerkiksi niiden luomis- tai viimeisimmän muokkauspäivämäärän tai otsikoiden aakkosjärjestyksen mukaan.

Käyttäjä voi merkitä muistiinpanon tähdellä, mikä tarkoittaa, että kyseinen muistiinpano on tärkeä.

Käyttäjä voi myös luoda kansioita, joihin hän voi lisätä haluamiaan muistiinpanoja.

Tietokantatauluja ovat  1. käyttäjät (jossa on eri käyttäjätunnukset), 2. käyttäjien otsikot, 3. muistiinpanot (sisältäen otsikot ja niiden sisällöt), 4. tähtimuistiinpanot ja 5. kansiot.

<br>

## Instructions
1. Make a .env file and copy the following content:
```
DATABASE_URL=<local-address-of-database>
SECRET_KEY=""
```
2. To generate the secret key:
```
python3 secretKey.py
```
And copy, paste the secret key into the .env

3. Activate the virtual environment and install the requirements
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
4.  Run the application using the command:
```
flask run

Tällä hetkellä sovellus pystyy kirjautumaan sisään ja luomaan uusia muistiinpanoja.