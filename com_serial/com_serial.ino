uint32_t deger = 0;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
deger += 1;
uint32_t zaman = millis();
Serial.print(zaman);
Serial.print("\t");
Serial.println(deger);
}
