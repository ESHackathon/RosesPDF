<template>
  <v-layout row>
    <v-flex sm12 md8 offset-md2>
      <v-stepper v-model="e6" vertical>
        <v-stepper-step step="1" :complete="e6 > 1">
          Title
          <small>The title must indicate that it is a systematic review protocol, and must indicate if it is an
            update/amendment: e.g. "A systematic review update protocol...".
          </small>
        </v-stepper-step>
        <v-stepper-content step="1">
          <v-form v-model="valid" ref="form" lazy-validation>
            <v-text-field
              label="Title"
              v-model="title"
              :rules="titleRules"
              :counter="10"
              required
            ></v-text-field>
          </v-form>
          <v-btn color="primary" @click.native="e6 = 2">Continue</v-btn>
          <v-btn flat>Cancel</v-btn>
        </v-stepper-content>

        <v-stepper-step step="2" :complete="e6 > 2">
          Type of Review
          <small>Select one of the following types of review: systematic review, systematic review update, systematic
            review amendment, systematic review from a systematic map.
          </small>
        </v-stepper-step>
        <v-stepper-content step="2">
          <v-select
            label="Type Of Review"
            v-model="typeOfReview"
            :items="typeOfReviewOptions"
            :rules="[v => !!v || 'Item is required']"
            required
          ></v-select>
          <v-btn color="primary" @click.native="e6 = 3">Continue</v-btn>
          <v-btn flat>Cancel</v-btn>
        </v-stepper-content>

        <v-stepper-step step="3" :complete="e6 > 3">
          Author Contracts
          <small>The full names, institutional addresses, and email addresses for all authors must be provided.</small>
        </v-stepper-step>
        <v-stepper-content step="3">
          <v-select
            label="Authors Contracts"
            v-model="authorsContracts"
            :items="checklistOptions"
            :rules="[v => !!v || 'Item is required']"
            required
          ></v-select>
          <v-btn color="primary" @click.native="e6 = 4">Continue</v-btn>
          <v-btn flat>Cancel</v-btn>
        </v-stepper-content>

        <v-stepper-step step="4" :complete="e6 > 4">
          Abstract
          <small>Abstract must not exceed 350 words and must include two sections 1) Background, the context and purpose
            of the review, including the review question; 2) Methods, how the review will be conducted and the outputs
            that are expected (specifically mention search strategy, inclusion criteria, critical appraisal, data
            extraction and synthesis).
          </small>
        </v-stepper-step>
        <v-stepper-content step="4">
          <v-select
            label="Abstract"
            v-model="abstract"
            :items="checklistOptions"
            :rules="[v => !!v || 'Item is required']"
            required
          ></v-select>
          <v-btn color="primary" @click.native="e6 = 5">Continue</v-btn>
          <v-btn flat>Cancel</v-btn>
        </v-stepper-content>

        <v-stepper-step step="5" :complete="e6 > 5">
          Background
          <small>Describe the rationale for the review in the context of what is already known. Protocol must indicate
            why this study was necessary and what it aims to contribute to the field.
          </small>
        </v-stepper-step>
        <v-stepper-content step="5">
          <v-select
            label="Background "
            v-model="background"
            :items="checklistOptions"
            :rules="[v => !!v || 'Item is required']"
            required
          ></v-select>
          <v-btn color="primary" @click.native="e6 = 6">Continue</v-btn>
          <v-btn flat>Cancel</v-btn>
        </v-stepper-content>

        <v-stepper-step step="6" :complete="e6 > 6">
          Stakeholder Agreement
          <small>The planned/actual role of stakeholders throughout the review process (e.g. in the formulation of the
            question) must be described and explained (using a broad definition of ‘stakeholder’, including e.g.
            researchers, funders and other decision-makers)
          </small>
        </v-stepper-step>
        <v-stepper-content step="6">
          <v-select
            label="Stakeholder Agreement"
            v-model="stakeholderAgreement"
            :items="checklistOptions"
            :rules="[v => !!v || 'Item is required']"
            required
          ></v-select>
          <v-btn color="primary" @click.native="e6 = 7">Continue</v-btn>
          <v-btn flat>Cancel</v-btn>
        </v-stepper-content>

        <v-stepper-step step="7" :complete="e6 > 7">
          Objectives of the Review
          <small>Describe the primary question and secondary questions (when applicable).</small>
        </v-stepper-step>
        <v-stepper-content step="7">
          <v-select
            label="Objectives"
            v-model="objectivesOfTheReview.objectives"
            :items="checklistOptions"
            :rules="[v => !!v || 'Item is required']"
            required
          ></v-select>
          <v-form v-model="valid" ref="form" lazy-validation>
            <v-text-field
              label="Definitions of the Question Component"
              v-model="objectivesOfTheReview.definitionsOfTheQuestionComponent"
              :rules="titleRules"
              :counter="10"
              required
            ></v-text-field>
          </v-form>
          <v-btn color="primary" @click.native="e6 = 8">Continue</v-btn>
          <v-btn flat>Cancel</v-btn>
        </v-stepper-content>

        <v-stepper-step step="8" :complete="e6 > 8">
          Submit Form
          <small>Already we will generate your .pdf report</small>
        </v-stepper-step>
        <v-stepper-content step="8">
          <v-btn
            @click="submit"
            :disabled="!valid"
          >
            submit
          </v-btn>
          <v-btn @click="clear">clear</v-btn>
        </v-stepper-content>
      </v-stepper>
    </v-flex>
  </v-layout>
</template>

<script>
  import download from 'downloadjs'

  export default {
    name: 'systematic-review-protocol',
    data () {
      return {
        message: 'Hi Vue!',
        e6: 1,
        valid: true,
        title: '',
        titleRules: [
          v => !!v || 'Title is required',
          v => (v && v.length <= 10) || 'Title must be less than 10 characters'
        ],
        typeOfReview: null,
        typeOfReviewOptions: [
          'Systematic Review',
          'Systematic Review Update',
          'Systematic Review Amendment',
          'Systematic Review from Systematic Map'
        ],
        authorsContracts: false,
        abstract: false,
        background: false,
        stakeholderAgreement: false,
        checklistOptions: [
          'Yes',
          'No',
          'N/A'
        ],
        objectivesOfTheReview: {
          objectives: '',
          definitionsOfTheQuestionComponent: ''
        }
      }
    },
    methods: {
      submit () {
        if (this.$refs.form.validate()) {
          // Native form submission is not yet supported
          const data = {
            title: this.title,
            typeOfReview: this.typeOfReview,
            authorsContracts: this.authorsContracts,
            background: this.background,
            stakeholderAgreement: this.stakeholderAgreement,
            objectivesOfTheReview: this.objectivesOfTheReview
          }
          this.axios.post('http://127.0.0.1:5000/', data, {
            responseType: 'blob',
            headers: {
              'Accept': 'application/pdf'
            }
          }).then((resp) => {
            download(resp.data, 'Report.pdf')
          })
        }
      },
      clear () {
        this.$refs.form.reset()
      }
    }
  }
</script>

<style lang="scss" scoped>
</style>
