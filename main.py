const Discord = require('discord.js');
const client = new Discord.Client();
const prefix = '+';

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}`);
});

client.on('message', async (message) => {
  if (!message.content.startsWith(prefix) || message.author.bot) return;

  const args = message.content.slice(prefix.length).trim().split(/ +/);
  const command = args.shift().toLowerCase();

  if (command === 'mute') {
    if (!message.member.hasPermission('MANAGE_ROLES')) {
      return message.channel.send('Vous n\'avez pas la permission de gérer les rôles.');
    }

    const member = message.mentions.members.first();
    if (!member) {
      return message.channel.send('Membre invalide.');
    }

    let mutedRole = message.guild.roles.cache.find(role => role.name === 'Muted');
    if (!mutedRole) {
      try {
        mutedRole = await message.guild.roles.create({
          data: {
            name: 'Muted',
            permissions: []
          }
        });

        message.guild.channels.cache.forEach(async (channel) => {
          await channel.updateOverwrite(mutedRole, {
            SEND_MESSAGES: false,
            ADD_REACTIONS: false
          });
        });
      } catch (error) {
        console.error(error);
        return message.channel.send('Une erreur s\'est produite lors de la création du rôle "Muted".');
      }
    }

    await member.roles.add(mutedRole);
    return message.channel.send(`${member} a été rendu muet.`);
  }

  // Ajoutez les autres commandes ici

});

// Remplacez 'TOKEN' par le token de votre bot
client.login('MTEyMzI1MDAzNjQ0MTEwNDU1NQ.Gvxbei.BuNBT1rQcyvvS1y6p0oEtIduZydUwG80J_jvEs');
