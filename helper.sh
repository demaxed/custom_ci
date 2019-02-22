#asserting

custom_asserting()
{
    local explanation=$1
    shit 1
    "$@"

    if [$? != 0]; then
        echo $explanation 1>&2
        exit 1
    fi
}