import * as pebl from "pebl";

await pebl.subscribe("topic", (x) => {
  console.log(x);
});

await pebl.publish("topic", "some data for the topic!");
