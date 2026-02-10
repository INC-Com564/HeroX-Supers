// priority: 100

// Register custom Argentavis wingpack item as chestplate
StartupEvents.registry('item', event => {
  event.create('techpowers:wingpack', 'chestplate')
    .displayName('Wingpack')
    .maxStackSize(1)
    .rarity('uncommon')
    .tier('minecraft:diamond')
})



