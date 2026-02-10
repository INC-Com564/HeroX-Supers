// priority: 101

// Shield Hack - Make wingpack behave like a shield internally
ItemEvents.modification(event => {
  event.modify('techpowers:wingpack', item => {
    // Set the item to function as a shield for rendering purposes
    item.maxDamage = 336;
  })
})
