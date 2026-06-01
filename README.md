# PokeAPI Automation Testing Plan

### 1. test_get_pokemon — Get a Pokemon
* **Request:** GET to `https://pokeapi.co/api/v2/pokemon/pikachu`
* **Assertions:**
  * Status code is `200`
  * `name` equals `"pikachu"`
  * Response contains fields: `height`, `weight`, `abilities`

### 2. test_abilities_is_list — Verify Pokemon Abilities
* **Request:** Same GET request (Pikachu)
* **Assertions:**
  * `abilities` field is a `list`
  * Total number of abilities is greater than `0`
  * Each item in the abilities list contains an `ability` field

### 3. test_get_pokemon_list — Get Pokemon List
* **Request:** GET to `/pokemon?limit=10`
* **Assertions:**
  * Status code is `200`
  * Response contains a `results` field
  * Total number of returned objects is exactly `10`
  * Each pokemon object has `name` and `url` fields

### 4. test_get_berry — Get a Berry
* **Request:** GET to `/berry/cheri`
* **Assertions:**
  * Status code is `200`
  * `name` equals `"cheri"`
  * Response contains a `growth_time` field
  * `growth_time` value is an `integer` (int)

### 5. test_not_found — Verify 404 Error Handling
* **Request:** GET to `/pokemon/fakemonster123`
* **Assertions:**
  * Status code is `404`