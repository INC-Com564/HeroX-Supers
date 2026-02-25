// Ensures AlienEvo timer objective always exists to prevent detransform script crashes.

const AEO_TIMER_OBJECTIVE = 'AlienEvo.Timer'

function ensureAlienEvoTimer(server) {
  server.runCommandSilent(`scoreboard objectives add ${AEO_TIMER_OBJECTIVE} dummy`)
}

ServerEvents.loaded(event => {
  ensureAlienEvoTimer(event.server)
})

PlayerEvents.loggedIn(event => {
  ensureAlienEvoTimer(event.server)
})

ServerEvents.tick(event => {
  if (event.server.tickCount % 200 !== 0) return
  ensureAlienEvoTimer(event.server)
})
