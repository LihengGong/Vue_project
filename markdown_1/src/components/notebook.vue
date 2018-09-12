<template>
  <div class="notebook" id="notebook">
    <aside class="side-bar">
      <div class="toolbar">
        <button :title="addNoteButtonTitle" @click="addNote"><i class="material-icons">+</i> Add note</button>
      </div>
      <div class="notes">
        <!-- notes -->
        <div class="note" v-for="(note, index) in notes" @click="selectNote(note)" :key="index">
          {{note.title}}
        </div>
      </div>
    </aside>
    <template v-if="selectedNote">
    <section class="main">
      <label for="title-input"></label>
      <input type="text" id="title-input" v-model="selectedNote.title"/>
      <label for="text-content"></label>
      <textarea v-model="selectedNote.content" id="text-content" rows="40"></textarea>
      <button class="primary" @click="saveSelected" id="save-button">Save</button>
    </section>
    <aside class="preview" v-html="notePreview"></aside>
    </template>
  </div>
</template>

<script>
// import axios from 'axios'
import Vue from 'vue'
import VueResource from 'vue-resource'
import marked from '../../static/marked'
const baseURL = 'http://127.0.0.1:8000/api/v1/'

Vue.use(VueResource)

export default {
  name: 'notebook',
  data () {
    return {
      notes: [],
      selectedId: null
    }
  },
  computed: {
    notePreview () {
      if (this.selectedNote.content) {
        return this.selectedNote ? marked(this.selectedNote.content) : ''
      } else {
        return ''
      }
    },
    addNoteButtonTitle () {
      return this.notes.length + ' note(s) already'
    },
    selectedNote () {
      return this.notes.find(note => note.id === this.selectedId)
    }
  },
  mounted () {
    this.getAllNotes()
  },
  methods: {
    addNote () {
      // const time = Date.now()
      // let note = {
      //   // id: String(time),
      //   title: 'New note' + (this.notes.length + 1),
      //   content: 'Write your **note** *here*',
      //   created: time,
      //   favorite: false
      // }

      let newNote = {
        title: 'New note ' + (this.notes.length + 1),
        content: 'Write your **note** *here*'
      }
      this.$http.post(baseURL, newNote)
        .then((response) => {
          console.log('Response from post is: ' + response.data)
          let createdNote = JSON.parse(JSON.stringify(response.data))
          console.log('Newly created: ' + createdNote)
          this.notes.push(createdNote)
          console.log('After adding new, now notes are: ' + this.notes)
        })
        .catch((response) => {
          console.log('Error from post is: ' + response.responseText)
        })
      // this.notes.push(note)
      // this.getAllNotes()
    },
    selectNote (note) {
      this.selectedId = note.id
    },
    getAllNotes () {
      this.$http.get(baseURL)
        .then((response) => {
          console.log('response: ' + response.data.toString())
          console.log('response length: ' + response.data.length)
          console.log('object 1: ' + JSON.stringify(response.data[0]))
          console.log('object 2: ' + JSON.stringify(response.data[1]))
          for (let i = 0; i < response.data.length; i++) {
            this.notes.push(JSON.parse(JSON.stringify(response.data[i])))
          }
          // console.log(this.notes)
        })
    },
    saveSelected () {
      console.log('selectedNote: ' + this.selectedNote)
      this.$http.put(baseURL + this.selectedNote.id + '/', this.selectedNote)
        .then((response) => {
          console.log('post succeeded. response is: ' + response.data)
        })
        .catch((response) => {
          console.log('Error: response is: ' + response.responseText)
        })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
body {
  font-family: sans-serif;
  font-size: 16px;
  height: 100%;
  margin: 0;
  box-sizing: border-box;
}

.material-icons {
  font-size: 24px;
  line-height: 1;
  vertical-align: middle;
  margin: -3px;
  padding-bottom: 1px;
}

#notebook > * {
  float: left;
  display: flex;
  flex-direction: column;
  height: 100%;

  > * {
    flex: auto 1 1;
  }
}

#save-button {
  width: 50%;
  background: dodgerblue;
}

.side-bar {
  background: #f8f8f8;
  width: 20%;
  box-sizing: border-box;
}

.note {
  padding: 16px;
  cursor: pointer;
}

.note:hover {
  background: #ade2ca;
}

.note .icon {
  float: right;
}

button,
input,
textarea {
  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
  box-sizing: border-box;
  outline: none !important;
}

button,
.note.selected {
  background: #40b883;
  color: white;
}

button {
  border-radius: 3px;
  border: none;
  display: inline-block;
  padding: 8px 12px;
  cursor: pointer;
}

button:hover {
  background: #63c89b;
}

input {
  border: solid 2px #ade2ca;
  border-radius: 3px;
  padding: 6px 10px;
  background: #f0f9f5;
  color: #666;
}

input:focus {
  border-color: #40b883;
  background: white;
  color: black;
}

button,
input {
  height: 34px;
}

.main, .preview {
  width: 40%;
}

.toolbar {
  padding: 4px;
  box-sizing: border-box;
}

.status-bar {
  color: #999;
  font-style: italic;
}

textarea {
  resize: none;
  border: 0.2rem solid gray;
  box-sizing: border-box;
  margin: 0 4px;
  font-family: monospace;
  height: auto;
}

textarea, .notes, .preview {
  flex: auto 1 1;
  overflow: auto;
}

.preview {
  padding: 12px;
  box-sizing: border-box;
  border-left: solid 4px #f8f8f8;
}

.preview p:first-child {
  margin-top: 0;
}

a {
  color: #40b883;
}

h1,
h2,
h3 {
  margin: 10px 0 4px;
  color: #40b883;
}

h1 {
  font-size: 2em;
}

h2 {
  font-size: 1.5em;
}

h3 {
  font-size: 1.2em;
}

h4 {
  font-size: 1.1em;
  font-weight: normal;
}
</style>
