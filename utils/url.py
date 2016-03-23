import re


def basic_url(s):
    """
    Converts basic url syntax to regex
    :param s: hello/{id}/{name}
    :return: hello/(?P<id>[^\/;]+)/(?P<name>[^\/;]+)/$
    """
    return "/".join(["/".join([token for token in s.split('/') if not re.search('{(.*)}', token)]), "/".join(
            ["(?P<" + param + ">[^\/;]+)" for param in
             [re.search('{(.*)}', token).group(1) for token in s.split('/') if re.search('{(.*)}', token)]]), "$"])
