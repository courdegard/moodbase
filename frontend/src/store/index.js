import { createStore } from 'vuex'
import { auth } from './auth.module'
import { wheelLock } from './visualization.module'
import { moodClassification } from './classification.module'
import { userData } from './user.data.module'
import { butts } from './weight.module'
import { communityData } from './community.data.module'
import { plotPage } from './plot.page.module'
import { groupCreator } from './group.creator'
import createPersistedState from 'vuex-persistedstate'

const store = createStore({
  modules: {
    auth,
    plotPage,
    wheelLock,
    moodClassification,
    userData,
    communityData,
    groupCreator,
    butts
  },
  plugins: [createPersistedState({
    paths: ['auth', 'userData', 'communityData', 'butts']
  })]

})

export default store
