#Open API REST (Python) - Lernfeld 9

##Endpoints

| METHOD | ENDPOINT                      | DESCRIPTION                                               | PARAMETER  | RESPONSE |
|--------|-------------------------------|-----------------------------------------------------------|---|---|
| GET    | /list/{:id}                   | Liefert alle Einträge einer Todo-Liste zurück.            | URL-Element: ID der gewünschten Liste. | JSON-Objekt |
| DELETE | /list/{:id}/delete            | Löscht eine komplette Todo-Liste mit allen Einträgen.     | URL-Element: ID der gewünschten Liste. | HTTP 200/404  |
| POST   | /list/add                     | Fügt eine neue Todo-Liste hinzu.                          |   |   |
| POST   | /list/{:id}/add/entry         | Fügt einen Eintrag zu einer bestehenden Todo-Liste hinzu. |   |   |
| POST   | /list/{:id}/edit/{:entryId}   | Aktualisiert einen bestehenden Eintrag.                   |   |   |
| DELETE | /list/{:id}/delete/{:entryId} | Löscht einen einzelnen Eintrag einer ToDo Liste.          |   |   |
| GET    | /user/get                     | Liefert eine Liste aller Benutzer zurück.                 |   |   |
| POST   | /user/add                     | Fügt einen neuen Benutzer hinzu.                          |   |   |
| POST   | /user/{id}/delete             | Löscht einen Benutzer.                                    |   |   |
