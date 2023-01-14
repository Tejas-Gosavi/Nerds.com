<template>
    <!-- <div class="mt-3 d-flex justify-content-center">
        {% if paginator %}
            <ul class="pagination">
                {% if products.has_previous %}
                    <li class="page-item">
                        <a class="page-link" href="{{ request.path }}?{% paginatedURL request.GET products.previous_page_number %}">&laquo;</a>
                    </li>
                {% else %}
                    <li class="page-item disabled">
                        <a class="page-link" href="#">&laquo;</a>
                    </li>
                {% endif %}

                {% for page in paginator.page_range %}
                    {% if current_page == page %}
                        <li class="page-item active">
                            <a class="page-link" href="{{ request.path }}?{% paginatedURL request.GET page %}">{{ page }}</a>
                        </li>
                    {% else %}
                        <li class="page-item">
                            <a class="page-link" href="{{ request.path }}?{% paginatedURL request.GET page %}">{{ page }}</a>
                        </li>
                    {% endif %}
                {% endfor %}

                {% if products.has_next %}
                    <li class="page-item">
                        <a class="page-link" href="{{ request.path }}?{% paginatedURL request.GET products.next_page_number %}">&raquo;</a>
                    </li>
                {% else %}
                    <li class="page-item disabled">
                        <a class="page-link" href="#">&raquo;</a>
                    </li>
                {% endif %}
            </ul>
        {% endif %}
    </div> -->
</template>