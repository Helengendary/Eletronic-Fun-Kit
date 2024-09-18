// C++ code
//
int vermelho = 12;
int verde = 8;
int Tensao = 0;
float velocidade = 0;
int pot = A5;
int potLuz = A4;
int branco = 10;
int laranja = 11;
int j = 0;
int luz = 0;
int luzContrario = 0;
int ledBotaun = 2;
int buttonNormal = 4;
int buttonPisca = 3;
int buttonPiscaRapido = 5;
int state = 0;
bool apertado = false;

void setup()
{
  pinMode(vermelho, OUTPUT);
  pinMode(branco, OUTPUT);
  pinMode(laranja, OUTPUT);
  pinMode(verde, OUTPUT);
  pinMode(ledBotaun, OUTPUT);
  pinMode(buttonNormal, INPUT);
  Serial.begin(9500);
}

void loop()
{
  	/*Tensao = map(analogRead(pot), 0, 1023, 0, 5);
	velocidade = map(analogRead(pot), 0, 1023, 100, 2000);
  	Serial.print(Tensao);
 	Serial.print("V\n");
  
    digitalWrite(vermelho, HIGH);
    digitalWrite(verde, LOW);
    delay(velocidade);
    digitalWrite(vermelho, LOW);
    digitalWrite(verde, HIGH);
    delay(velocidade);*/
  
  /*j = 255;

    
  for ( int i = 0; i < 255; i++){
  	analogWrite(branco, i);
    analogWrite(laranja, j);
    j--;
    delay(map(analogRead(potLuz), 0, 1023, 10, 70));
  }
  
  for ( int i = 254; i > 0; i--){
  	analogWrite(branco, i);
    analogWrite(laranja, j);
    j++;
    delay(map(analogRead(potLuz), 0, 1023, 10, 70));
  }*/
  
  /*luz = map(analogRead(potLuz), 0, 1023, 0, 255);
  
  analogWrite(branco, luz);
  analogWrite(laranja, (255-luz));
  Serial.println(luz);*/
  
  if (!digitalRead(buttonNormal)){
  	apertado = false;
  }
 
  if (digitalRead(buttonNormal) && !apertado){
  	state++;
    apertado = true;
  }
  
  if (state == 4) {
  	state = 0;
  }
  
  Serial.println();
  delay(10);
  
  if (state == 1) {
  	digitalWrite(ledBotaun, LOW);
  } else {  
	if (state == 2) {
      
      digitalWrite(ledBotaun, LOW);
      delay(1000);
      digitalWrite(ledBotaun, HIGH);
      delay(1000);
    } else {  
		if (state == 3) {
          digitalWrite(ledBotaun, LOW);
          delay(300);
          digitalWrite(ledBotaun, HIGH);
          delay(300);
        } else { 
        	digitalWrite(ledBotaun, HIGH);
        }
    }
  }
    
}
