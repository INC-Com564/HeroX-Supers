// priority: 100

// Register Surge Claws as Curios hands item
StartupEvents.registry('item', event => {
  event.create('enhanced:surge_claws')
    .displayName('Surge Claws')
    .maxStackSize(1)
    .rarity('rare')
})
