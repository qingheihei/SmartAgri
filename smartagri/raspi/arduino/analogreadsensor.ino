void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  Serial.println("Starting WD-3-WET-5Y Test");
}

// the loop routine runs over and over again forever:
void loop() {
  delay(2000);
  float W = analogRead(A0);
  float EC = analogRead(A1);
  float T = analogRead(A2);
  // print out the value you read:
  if(isnan(W) || isnan(EC) || isnan(T)){
    Serial.println("Failed to read from WD-3-WET-5Y!");
  }
  String postData = "{'Humid':";
  postData.concat(W);
  postData.concat(", 'EC':");
  postData.concat(EC);
  postData.concat(", 'Temp':");
  postData.concat(T);
  postData.concat("}");
  Serial.println(postData);
}
