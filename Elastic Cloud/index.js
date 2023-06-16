
const { Client } = require('@elastic/elasticsearch')
const config = require('config');
const elasticConfig = config.get('elastic-cloud');

//Create client
const client = new Client({
  node: elasticConfig.node,
  auth: {
    username: elasticConfig.username,
    password: elasticConfig.password
  }
})


client.info()
  .then(response => console.log(response))
  .catch(error => console.error(error))

// insert info into elastic index
// async function run() {
//     await client.index({
//         index: 'game-of-thrones',
//         body: {
//             character: 'Ned Stark',
//         quote: 'Winter is coming.'
//         }
//     })

//     await client.index({
//         index: 'game-of-thrones',
//         body: {
//             character: 'Daenerys Targaryen',
//         quote: 'I am the blood of the dragon.'
//         }
//     })

//     await client.index({
//         index: 'game-of-thrones',
//         body: {
//             character: 'Tyrion Lannister',
//         quote: 'A mind needs books like a sword needs whetstone.'
//         }
//     })

//     await client.indices.refresh({index: 'game-of-thrones'})
// }


// read the elastic index
// async function read() {
//     const body = await client.search({
//       index: 'autos',
//     //   headers: { Authorization: `ApiKey ${'SVpCTktZZ0JHeFRLNXZ2ZGhUdWo6Q2czd3JaSHVSTkdsN2l2Y01GRTJGdw=='}` },
//       body: {
//         query: {
//           match: { quote: 'kia' }
//         }
//       }
//     })
//     console.log(body)
// }
  
// read().catch(console.log)
  

// Generate API keys
async function generateApiKeys (opts) {
    const body = await client.security.createApiKey({
      body: {
        name: 'Update elastic gerry dev',
        role_descriptors: {
          'nodejs_example_writer': {
            'cluster': ['monitor'],
            'index': [
              {
                'names': ['autos_dev'],
                'privileges': ['create_index', 'write', 'read', 'manage']
              }
            ]
          }
        }
      }
    })
  
    return Buffer.from(`${body.id}:${body.api_key}`).toString('base64')
}

generateApiKeys()
    .then(console.log)
    .catch(err => {
    console.error(err)
    process.exit(1)
})

// run().catch(console.log)
  