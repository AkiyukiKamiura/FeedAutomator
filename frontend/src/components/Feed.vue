<template>
  <div class="container-fruid">
    <b-row>
      <b-col cols='4'>
        <b-card class='feed-card'
          v-for="(feed, index) in feeds"
          :key='index'
          :title='feed.name'
        >
          <div class='card-content'>
            <div class='description'>{{ feed.description }}</div>
            <div class='url'>{{ feed.url }}</div>
          </div>
          <b-button href="#" squared variant="outline-primary" @click='getEntries(feed.id)'>See Entries</b-button>
          <b-button href="#" squared variant="outline-warning">Load Entries Now</b-button>
          <b-button href="#" squared variant="outline-success">Edit</b-button>
        </b-card>
      </b-col>

      <b-col cols='8'>
        <b-list-group>
          <b-list-group-item
            v-for="(entry, index) in entries"
            :href='entry.url'
            target="_blank"
            :key='index'
          >
            <div class="d-flex w-100 justify-content-between">
              <h5 class="mb-1">{{ entry.title }}</h5>
              <small>{{ entry.published }}</small>
            </div>
            <p class="mb-1">
              {{ entry.content }}
            </p>
            <small>{{ entry.url }}</small>
          </b-list-group-item>
        </b-list-group>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      feeds: [],
      entries: [],

      showedFeedId: null,
      entryUrl: null
    }
  },
  methods: {
    getFeeds () {
      // FIX: THIS IS LOCALIZED
      const path = 'http://localhost:5000/api/feeds/get'
      axios.get(path)
        .then(response => {
          this.feeds = response.data
        })
        .catch(error => {
          console.log(error)
        })
    },
    getEntries (feed_id) {
      const path = 'http://localhost:5000/api/feeds/' + feed_id + '/entries'
      this.showedFeedId = feed_id

      axios.get(path)
        .then(response => {
          this.entries = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  created () {
    this.getFeeds()
  }
}
</script>

<style>
.feed-card {
  width: 100%;
}

.card-content {
  margin: 0 auto;
}

.url {
  text-align: left;
  /* color: gray; */
  font-size: 14px;
  margin-bottom: 10px;
}

.description {
  text-align: left;
  /* color: gray; */
  font-size: 18px;
  margin-bottom: 10px;
}
</style>
