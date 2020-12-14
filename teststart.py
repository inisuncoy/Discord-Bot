client.player

.on('trackStart', (message, track) => message.channel.send(`Now playing ${track.title}...`))
.on('trackAdd', (message, track) => message.channel.send(`${track.title} has been added to the queue!`))
.on('playlistAdd', (message, playlist) => message.channel.send(`${playlist.title} has been added to the queue (${playlist.items.length} songs)!`))
.on('searchResults', (message, query, tracks) => {
 
    const embed = new Discord.MessageEmbed()
    .setAuthor(`Here are your search results for ${query}!`)
    .setDescription(tracks.map((t, i) => `${i}. ${t.title}`))
    .setFooter('Send the number of the song you want to play!')
    message.channel.send(embed);
 
})
