function makeNode(ch) {
    this.ch = ch;
    this.isTerminal = false;
    this.map = {};                                     // making node
    this.words = [];
}

function add(str, i, root) {

    if (i === str.length) {
        root.isTerminal = true;                        // to stop when the complete word is entered
        return;
    }
    if (!root.map[str[i]])                             //if that letter is not in trie create a node if it has app and if we need to add l
        root.map[str[i]] = new makeNode(str[i]);

    root.words.push(str);                               
    add(str, i + 1, root.map[str[i]]);
}

function search(str, i, root) {
    if (i === str.length)
        return root.words;

    if (!root.map[str[i]])					//if we are searching for a word whose prefix is not in tree then return none
        return [];                                   
    return search(str, i + 1, root.map[str[i]]);	// perform reccursions


}