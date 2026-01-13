# Maybe-as-a-Service (MaaS)

> *Commitment issues? There's an API for that.*

## What is Maybe-as-a-Service?

MaaS is the missing piece in the holy trinity of decision-making APIs. While Yes-as-a-Service gives you definitive answers and [No-as-a-Service](https://github.com/hotheadhacker/no-as-a-service) shuts things down, Maybe-as-a-Service embraces the beautiful ambiguity of indecision.

Perfect for:
- Decision bots that need to sound more human
- UI placeholders that capture the user experience
- Corporate meeting simulators
- Adding delightful uncertainty to your applications
- Philosophical contemplation APIs

```
  __  __             _          
 |  \/  |           | |         
 | \  / | __ _ _   _| |__   ___ 
 | |\/| |/ _` | | | | '_ \ / _ \
 | |  | | (_| | |_| | |_) |  __/
 |_|  |_|\__,_|\__, |_.__/ \___|
                __/ |           
               |___/            
    as-a-Service
```

## Quick Start

```bash
git clone https://github.com/B3ns44d/maybe-as-a-service.git
cd maybe-as-a-service

pip install -r requirements.txt

uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Get Random Maybe
```bash
curl http://localhost:8000/maybe
```
```json
{
  "response": "Maybe yes, maybe no, maybe I'll decide tomorrow.",
  "id": 1,
  "category": "procrastinator"
}
```

### Get Specific Response
```bash
curl http://localhost:8000/maybe/5
```

### Filter by Category
```bash
curl http://localhost:8000/maybe/category/philosophical
```

Available categories:
- `philosophical` - Existential musings
- `corporate` - Business jargon gold
- `passive-aggressive` - Subtle shade
- `procrastinator` - Classic delay tactics
- `quantum` - Science-themed uncertainty
- `commitment-phobic` - Relationship energy

### Health Check
```bash
curl http://localhost:8000/health
```
```json
{
  "status": "maybe"
}
```

## Interactive Documentation

Visit `http://localhost:8000/docs` for the auto-generated Swagger UI documentation, or `http://localhost:8000/redoc` for ReDoc-style docs.

## Example Integrations

### JavaScript/Node.js
```javascript
const response = await fetch('https://your-api.com/maybe');
const maybe = await response.json();
console.log(maybe.response); // "I exist in a superposition of yes and no until observed."
```

### Python
```python
import requests

response = requests.get('https://your-api.com/maybe/category/corporate')
print(response.json()['response'])  # "Let's circle back on that after the next quarterly review."
```

### cURL
```bash
# Get a philosophical maybe
curl -X GET "https://your-api.com/maybe/category/philosophical" \
     -H "accept: application/json"
```

## Contributing New Maybes

We welcome contributions of witty, ambiguous responses! Here's how:

1. Fork the repository
2. Add your responses to `responses.json` following this format:
```json
{
  "id": 21,
  "response": "Your delightfully ambiguous response here",
  "category": "one-of-the-existing-categories"
}
```
3. Ensure your response is:
   - Clever and relatable
   - Appropriately ambiguous
   - Safe for work
   - Between 10-100 characters ideally
4. Submit a pull request with a description of your additions

### Response Guidelines
- **Philosophical**: Think existential, cosmic, or deep
- **Corporate**: Business buzzwords and meeting-speak
- **Passive-Aggressive**: Subtle, polite shade
- **Procrastinator**: Delay tactics and "later" vibes
- **Quantum**: Science and physics themed
- **Commitment-Phobic**: Relationship avoidance energy