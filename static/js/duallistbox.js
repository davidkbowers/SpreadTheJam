      let dualListbox = new DualListbox("#select1"); // Selects the first element with the id 'select'

      function btnsub() {
        console.log("duh");
        var x = document.getElementById("select1");
        var txt = "";
        var txt1 = "";
        var txt2 = "";
        var i;
        for (i = 0; i < x.length; i++) {
          txt = txt + x.options[i].text + ",";
          txt1 = txt1 + x.options[i].value + ",";
          txt2 = txt2 + "{value:" + x.options[i].value + " text:" + x.options[i].text +"}";
        }
        console.log({txt});
        console.log({txt1});
        console.log({txt2});

        var xmlhttp = new XMLHttpRequest();   // new HttpRequest instance
        xmlhttp.open("POST", "https://jsonplaceholder.typicode.com/posts");
        xmlhttp.setRequestHeader("Content-Type", "application/json");
        xmlhttp.send(JSON.stringify(txt2));

    }
