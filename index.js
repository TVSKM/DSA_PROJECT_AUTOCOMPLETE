const items = [
    "an",
    "apple",
    "ancestor",
    "anger",
    "bag",
    "ball",
    "bell",
    "cat",
    "catch",
    "calm",
    "dog",
    "donkey",
    "drum",
    "fun",
    "fish",
    "french",
    "ice",
    "ink",
    "india",
    "man",
    "monkey",
    "money",
    "rat",
    "ram",
    "rabbit",
    "temple",
    "tent",
    "truck",
    "van",
    "vaccine",
    "visa",
    "pen",
    "pluto",
    "penguin",
    "python",
    "save",
    "south",
    "send",
    "water",
    "ground",
    "game",
    "gun",
    "honey",
    "hut",
    "hit",
    "up",
    "under",
    "ubuntu",
    "you",
    "yards",
    "year",
    "ear",
    "electric",
    "elephant"
];

const root = new makeNode('\0');         				//adding words into trie
for (const item of items)
    add(item, 0, root);

const text_box = document.getElementById("text-box");
const list = document.getElementById("list");

function handler(e) {
    const str = e.target.value;
    const predictions = search(str, 0, root);

    console.log(predictions);
     
    list.innerHTML = "";						//resetting list always
    for (const prediction of predictions)
        list.innerHTML += `<li class="list-group-item clickable" onclick="handleClick(this)"><b>${str}</b>${prediction.substring(str.length)}</li>`;    //here we are trying to give on click property

}

function handleClick(e) {
    text_box.value = e.innerText;
}

handler({ target: { value: "" } });


text_box.addEventListener("keyup", handler);