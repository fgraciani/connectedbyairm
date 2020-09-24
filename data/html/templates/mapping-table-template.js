var options = {
            valueNames: [
                'Concept',
                { attr: 'href', name:'html'},
                { attr: 'title', name:'Id'}, 
                'Definition', 
                'Correspondence', 
                { attr: 'href', name:'url'},
                { attr: 'title', name:'urn'}, 
                'Additional', 
                { attr: 'title', name:'addurn'},
                { attr: 'href', name:'addurl'}, 
                'Additional2', 
                { attr: 'href', name:'addurl2'}
                ],
            // Since there are no elements in the list, this will be used as template.
            //page: 10,
            //pagination: true,
			item: 
            `<tr>
                <td data-toggle="tooltip" data-placement="left" class="Id" style="word-wrap: break-word;min-width: 200px;max-width: 200px;">
                    <a class="html"> 
                        <p class="Concept">
                        </p>
                    </a>
                </td>
                <td class="Definition">
                </td>
                <td data-toggle="tooltip" data-placement="left" class="urn" style="word-wrap: break-word;min-width: 220px;max-width: 220px;"> 
                    <a target="_blank" class="url"> 
                        <p class="Correspondence">
                        </p>
                    </a>
                </td>
                <td data-toggle="tooltip" data-placement="left" class="addurn" style="word-wrap: break-word;min-width: 220px;max-width: 220px;"> 
                    <a target="_blank" class="addurl"> 
                        <p class="Additional">
                        </p>
                    </a>
                    <a target="_blank" class="addurl2"> 
                        <p class="Additional2">
                        </p>
                    </a>
                </td>
            </tr>`
        };

        var values = [] ;
        
        var termList = new List('mapping', options, values);