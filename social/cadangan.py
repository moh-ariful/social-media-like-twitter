
class PostDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm()

        context = {
            'post': post,
            'form': form,
        }

        return render(request, 'social/post_detail.html', context)

    def post(self, request, *args, **kwargs):
        pass
