Notes:
- docker-compose build
- docker-compose up

This is a self-contained little example data pipeline project.

1. Clone the code
2. Run the code (show a screenshot)
3. Show messages being passed between components (screenshot)
4. Show data populated in neo4j using the neo4j GUI at localhost: http://localhost:7474/browser/ (screenshot)
5. Use the elasticvue GUI (https://elasticvue.com/) to show the content of the elasticsearch index at localhost:9200 (screenshot). One message in the index should look like this: ```{
	"_index": "messages-test",
	"_type": "_doc",
	"_id": "d6oBbIoBmNUJVupvUGb-",
	"_version": 1,
	"_seq_no": 7,
	"_primary_term": 1,
	"found": true,
	"_source": {
		"content": "Message 29-2023-09-06 19:39:00.220912"
	}
}```
6. Explain in one printed page or less what this code does (text file)
7. Show a screenshot of the log messages from the running containers and explain how you would use these messages to debug the project/pipeline
